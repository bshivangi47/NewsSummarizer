import React, { useState } from "react";
import { Link } from "react-router-dom";
import AppBar from "@material-ui/core/AppBar";
import Box from "@material-ui/core/Box";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
function Navbar() {
  return (
    <>
      <div className="navbar">
        <Link to="#" className="menu-bars">
          <IconButton />
        </Link>
      </div>
    </>
  );
}

export default Navbar;
