import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./App";
import * as serviceWorker from "./serviceWorker";

// Use createRoot instead of render for React 17
ReactDOM.createRoot(document.getElementById("root")).render(<App />);

// If you want your app to work offline and load faster, 