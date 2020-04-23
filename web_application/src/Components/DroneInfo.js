import React from 'react'
import CircularProgress from '@material-ui/core/CircularProgress'
import SimpleTable from './DroneInfoTable'
import DeleteIcon from '@material-ui/icons/Delete'
import UpdateIcon from '@material-ui/icons/Update';
import Button from '@material-ui/core/Button'
import { makeStyles } from '@material-ui/core/styles'


const useStyles = makeStyles((theme) =>({
    table: {
      minWidth: 650,
    },
    button: {
      margin: theme.spacing(1),
      align: 'center',
    },
  }));

export default class DroneInfo extends (React.Component){
    constructor(){
        super()
        this.state = {
            isLoaded : false,
            items : []
        }
        this.updateHandler = this.updateHandler.bind(this)
        this.deleteHandler = this.deleteHandler.bind(this)
    }

    componentDidMount(){
        fetch('http://127.0.0.1:5000/getstatus')
        .then(respose => respose.json())
        .then(json => {
            this.setState({
                isLoaded : true,
                items : json,
            })
        }).catch(console.log)
    }

    updateHandler(){
        fetch('http://127.0.0.1:5000/getstatus')
        .then(respose => respose.json())
        .then(json => {
            this.setState({
                isLoaded : true,
                items : json,
            })
        }).catch(console.log)
        this.forceUpdate()
    }

    deleteHandler(){
        var requestOptions = {
            method: 'DELETE',
        };
        fetch('http://127.0.0.1:5000/delete', requestOptions)
            .then(response => response.json())
            .then(data => console.log("Number of rows deleted is/are :" + data.no_of_rows));
        this.forceUpdate()
    }

    render(){
        const classes = useStyles
        var {isLoaded, items} = this.state
        if (!isLoaded){
            return <CircularProgress color="secondary" />
        }

        return (
            <div>
                <SimpleTable items={items}/>
                <Button
                    variant="contained"
                    color="secondary"
                    className={classes.button}
                    startIcon={<DeleteIcon />}
                    align="right"
                    onClick={this.deleteHandler}
                    >
                Delete
                </Button>
                <Button
                variant="contained"
                color="primary"
                className={classes.button}
                startIcon={<UpdateIcon />}
                onClick={this.updateHandler}
                >
                    Update
                </Button>
            </div>
        )
    }
    
}
