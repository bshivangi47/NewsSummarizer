import Header from "./Header";
import React from "react";
import "./App.css";
import Home from "./pages/Home";
import Payment from "./pages/Payment"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Home />}></Route>
        <Route exact path="/payment" element={<Payment />}></Route>
      </Routes>
    </Router>
  );
}

export default App;
