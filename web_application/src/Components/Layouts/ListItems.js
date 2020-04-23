import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import AssignmentIcon from '@material-ui/icons/Assignment';
import BackupIcon from '@material-ui/icons/Backup';
import DashboardIcon from '@material-ui/icons/Dashboard';


export default function MainListItems(props){
  return(
    <div>
      <ListItem button onClick={() => props.onClickHandler()}>
        <ListItemIcon>
        <AssignmentIcon />
          </ListItemIcon>
        <ListItemText primary= "Scheduler" />
      </ListItem>
      <ListItem button onClick={() => props.handlerCreateTask()}>
        <ListItemIcon>
          <BackupIcon />
        </ListItemIcon>
        <ListItemText primary="Create Task" />
      </ListItem>
      <ListItem button>
        <ListItemIcon>
          <DashboardIcon />
        </ListItemIcon>
        <ListItemText primary="Video" />
      </ListItem>
    </div>
  )

}

