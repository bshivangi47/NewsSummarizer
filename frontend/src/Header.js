import * as React from "react";

// importing material UI components
import AppBar from "@material-ui/core/AppBar";
import Box from "@material-ui/core/Box";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import Menu from "@material-ui/core/Menu";
import {useNavigate} from "react-router-dom"

export default function Header() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const navigate=useNavigate()
  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleClick = (event) => {
    console.log("handling click!");
    setAnchorEl(event.currentTarget);
  };
  const NavigatePayment = (event) => {
    console.log("handling click!");
    navigate("/payment")
  };
  return (
    <AppBar position="static">
      <Toolbar>
        {/*Inside the IconButton, we
           can render various icons*/}
        <IconButton
          size="large"
          edge="start"
          color="inherit"
          aria-label="menu"
          sx={{ mr: 2 }}
        >
          {/*This is a simple Menu
             Icon wrapped in Icon */}
          <MenuIcon onClick={handleClick} />
        </IconButton>
        <Menu
          keepMounted
          anchorEl={anchorEl}
          onClose={handleClose}
          open={Boolean(anchorEl)}
        >
          <MenuItem onClick={handleClose}>Politics</MenuItem>
          <MenuItem onClick={handleClose}>Media</MenuItem>
          <MenuItem onClick={handleClose}>Opinion</MenuItem>
          <MenuItem onClick={handleClose}>Business</MenuItem>
          <MenuItem onClick={handleClose}>Entertainment</MenuItem>
          <MenuItem onClick={handleClose}>Sports</MenuItem>
          <MenuItem onClick={handleClose}>Lifestyle</MenuItem>
          <MenuItem onClick={handleClose}>Weather</MenuItem>
          <MenuItem onClick={handleClose}>Science</MenuItem>
        </Menu>

        {/* The Typography component applies
           default font weights and sizes */}

        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          News Category
        </Typography>
        <Button color="inherit" onClick={NavigatePayment}>Buy Premium membership</Button>
        
      </Toolbar>
    </AppBar>
  );
}
