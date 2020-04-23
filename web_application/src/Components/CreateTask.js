import React from 'react'
import CircularProgress from '@material-ui/core/CircularProgress'
import Input from '@material-ui/core/Input'
import Button from '@material-ui/core/Button'
import { makeStyles } from '@material-ui/core/styles'
import SaveIcon from '@material-ui/icons/Save';


const useStyles = makeStyles((theme) => ({
    root: {
      '& > *': {
        margin: theme.spacing(1),
      },
    },  
    button: {
        margin: theme.spacing(1),
      },

  }));


export default class CreateTask extends(React.Component){

    constructor(){
        super()
        this.state = {
            isLoaded : true,
            item_x : 0,
            item_y :0,
            destination_x:0,
            destination_y:0
        }
        this.submitHandler = this.submitHandler.bind(this)
    }

    itemXHandler = (event) => {
        this.setState({
            item_x : parseInt(event.target.value, 10)
        })
    }
    itemYHandler = (event) => {
        this.setState({
            item_y : parseInt(event.target.value, 10)
        })
    }
    destXHandler = (event) => {
        this.setState({
            destination_x : parseInt(event.target.value, 10)
        })
    }
    destYHandler = (event) => {
        this.setState({
            destination_y : parseInt(event.target.value, 10)
        })
    }

    submitHandler(){
        console.log(this.state)
        var requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify([this.state])
        };
        this.setState({
            isLoaded: false
        })
        fetch('http://127.0.0.1:5000/setstatus', requestOptions)
            .then(response => response.json())
            .then(data => this.setState({ isLoaded: true}));
    }

    componentDidMount(){
    }

    render(){
        const classes = useStyles
        var {isLoaded, items} = this.state
        if(!this.props.displayCreatTask){
            return <div></div>
        }

        if (!isLoaded){
            return <CircularProgress color="secondary" />
        }

        return (
            <div>
                <br />
                <form className={classes.root} noValidate autoComplete="off">
                    <h3>Create task for drones. Please enter the following information.</h3>
                    <Input placeholder="Enter the item's x-coordinate" inputProps={{ 'aria-label': 'description' }} onChange={this.itemXHandler}/>
                    <br />
                    <br />
                    <Input placeholder="Enter the item's y-coordinate" inputProps={{ 'aria-label': 'description' }} onChange={this.itemYHandler}/>
                    <br />
                    <br />
                    <Input placeholder="Enter the destination's x-coordinate"  inputProps={{ 'aria-label': 'description' }} onChange={this.destXHandler}/>
                    <br />
                    <br />
                    <Input placeholder="Enter the destination's y-coordinate"  inputProps={{ 'aria-label': 'description' }} onChange={this.destYHandler}/>
                    <br />
                    <br />
                    <Button
            variant="contained"
            color="primary"
            size="small"
            className={classes.button}
            startIcon={<SaveIcon />}
            onClick={this.submitHandler}
          >
            Save
          </Button>
                </form>
            </div>
        )
    }
}
