import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AssignmentIcon from '@material-ui/icons/Assignment';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';
import DashboardIcon from '@material-ui/icons/Dashboard';



export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon>
      <AssignmentIcon />
        </ListItemIcon>
      <ListItemText primary="Shceduler" />
    </ListItem>
    <ListItem button>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Video" />
    </ListItem>
      

  </div>
);