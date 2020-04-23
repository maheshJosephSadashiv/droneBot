import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import CssBaseline from '@material-ui/core/CssBaseline';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Scheduler from '../Scheduler'
import CreateTask from '../CreateTask'
import MainListItems from './ListItems';


const drawerWidth = 240;

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  appBar: {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
  },
  drawer: {
    width: drawerWidth,
    flexShrink: 0,
  },
  drawerPaper: {
    width: drawerWidth,
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.default,
    padding: theme.spacing(3),
  },
}));

function DrawerLeft(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <CssBaseline />
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <Typography variant="h6" noWrap>
            Swarm Copter
          </Typography>
        </Toolbar>
      </AppBar>
      <Drawer
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
        anchor="left"
      >
        <div className={classes.toolbar} />
        <Divider />
        <List>
          <div>
            <MainListItems onClickHandler={props.onClickHandler} handlerCreateTask={props.handlerCreateTask}/>
          </div>
        </List>
        <Divider />
      </Drawer>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        <Scheduler displayDBInfo={props.displayDBInfo} a/>
        <CreateTask displayCreatTask={props.createTaskInfo} a/>
      </main>
    </div>
  );
}

 
export default class PermanentDrawerLeft extends (React.Component){
  
  constructor(){
    super()
    this.state = {
      displayDBInfo : false,
      createTaskInfo : false
    }
    this.clickedHandler = this.clickedHandler.bind(this)
    this.handlerCreateTask = this.handlerCreateTask.bind(this)
  }

  handlerCreateTask(){
    if(this.state.createTaskInfo)
    this.setState({
      createTaskInfo : false
    })
  else
    this.setState({
      createTaskInfo : true
    })
  }

  clickedHandler(){
    if(this.state.displayDBInfo)
      this.setState({
        displayDBInfo : false
      })
    else
      this.setState({
        displayDBInfo : true
      })
 }

  render(){
    return <DrawerLeft displayDBInfo={this.state.displayDBInfo}
                       onClickHandler={this.clickedHandler}
                       createTaskInfo={this.state.createTaskInfo}
                       handlerCreateTask={this.handlerCreateTask}/>
  }
}