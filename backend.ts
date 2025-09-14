import dotenv from "dotenv";
dotenv.config();
import express from "express";
import { spawn } from "child_process";
import OpenAI from "openai";

const app = express();
app.use(express.json());

// Setup OpenAI
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY, // <-- paste key in .env
});

// Helper function to run a Python model
function runPythonModel(script: string, inputData: any): Promise<string> {
  return new Promise((resolve, reject) => {
    const pythonProcess = spawn("python", [script, JSON.stringify(inputData)]);

    let result = "";
    pythonProcess.stdout.on("data", (data) => {
      result += data.toString();
    });

    pythonProcess.stderr.on("data", (err) => {
      reject(err.toString());
    });

    pythonProcess.on("close", () => {
      resolve(result.trim());
    });
  });
}

// Prediction route
app.post("/predict", async (req, res) => {
  const inputData = req.body;

  try {
    // Run both Python models
    const prediction1 = await runPythonModel("model.ipynb", inputData);
    const prediction2 = await runPythonModel("modelv.ipynb", inputData);

    let advice = "✅ No disease detected. Cow is healthy.";

    // If disease found in model2, call OpenAI
    if (prediction2.toLowerCase() !== "healthy") {
      const completion = await client.chat.completions.create({
        model: "gpt-4o-mini",
        messages: [
          {
            role: "system",
            content:
              "You are a veterinary assistant for farmers. Give clear, step-by-step advice.",
          },
          {
            role: "user",
            content: `A cow has been diagnosed with ${prediction2}. Provide immediate steps the farmer should take.`,
          },
        ],
      });

      advice = completion.choices[0].message.content ?? "No advice available.";
    }

    // Send results from both models + advice
    res.json({
      model1_prediction: prediction1,
      model2_prediction: prediction2,
      advice,
    });
  } catch (error) {
    console.error("❌ Error:", error);
    res.status(500).send("Error running models");
  }
});

// Start server
app.listen(3000, () => {
  console.log("🚀 Server running on http://localhost:3000");
});
