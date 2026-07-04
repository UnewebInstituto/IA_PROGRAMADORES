require('dotenv').config();
const express = require('express');
const cors = require('cors');
const { GoogleGenerativeAI } = require("@google/generative-ai");

const app = express();
app.use(express.json());
app.use(cors());

const genAI = new GoogleGenerativeAI(process.env.API_KEY);

app.post('/api/pregunta', async (req, res) => {
    try {
        const { pregunta } = req.body;
        if (!process.env.API_KEY) throw new Error("API Key no configurada");
        const model = genAI.getGenerativeModel({ model: "gemini-3.5-flash" });
        const result = await model.generateContent(pregunta);
        res.json({ respuesta: result.response.text() });
    } catch (error) {
        console.error("Detalle del error:", error); // Esto aparecerá en tu terminal
        res.status(500).json({ error: "Error al conectar con la IA" });
    }
});

app.listen(3000, () => console.log('Backend en http://localhost:3000'));