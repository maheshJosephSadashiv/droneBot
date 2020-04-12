import React from "react";
import AppBar from "material-ui/AppBar";
import Toolbar from "material-ui/Toolbar";
import  Typography  from "material-ui/Typography";

export default props => (
  <AppBar position="static">
    <Toolbar>
      <Typography variant="h6">this header ...</Typography>
    </Toolbar>
  </AppBar>
);
