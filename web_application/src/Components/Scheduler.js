import React from 'react'
import DroneInfo from './DroneInfo'


export default class Scheduler extends (React.Component){
    
    render(){   
        if (this.props.displayDBInfo){
            return <DroneInfo />
        }

        else
            return (
                <div></div>
                ) 
    }
}



