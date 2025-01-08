
import express, { type Request, Response, NextFunction } from "express";
import { registerRoutes } from "./routes";
import { setupVite, serveStatic, log } from "./vite";
import dotenv from "dotenv";

// Load environment variables
dotenv.config();

const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

async function startServer() {
    try {
        const server = registerRoutes(app);
        
        if (process.env.NODE_ENV === "development") {
            await setupVite(app, server);
        } else {
            serveStatic(app);
        }

        const PORT = process.env.PORT || 5000;
        server.listen(PORT, "0.0.0.0", () => {
            log(`Server running on port ${PORT} in ${process.env.NODE_ENV} mode`);
        });
    } catch (error) {
        log(`Failed to start server: ${error.message}`);
        process.exit(1);
    }
}

startServer();
