import React from 'react';
import ReactDOM from 'react-dom';
import { render } from '@testing-library/react';
import App from './Components/App';
import {CreateTask} from './Components/CreateTask';
import {SimpleTable} from './Components/DroneInfoTable'
import {PermanentDrawerLeft} from './Components/Layouts/Drawer';
import {DroneInfo} from './Components/DroneInfo';
import {Scheduler} from './Components/Scheduler'



test('renders React App', () => {
    const div =document.createElement("div");
    ReactDOM.render(<App />,div);
});




it("Identifies all Components ",()=>{
    ReactDOM.findDOMNode(SimpleTable);
    ReactDOM.findDOMNode(CreateTask);
    ReactDOM.findDOMNode(PermanentDrawerLeft);
    ReactDOM.findDOMNode(DroneInfo);
    ReactDOM.findDOMNode(Scheduler);
});



const mockFn = jest.fn().mockImplementation((x1,y1,x2,y2) => {
    if(x1==null || x2==null || y1==null || y2==null){
        return false;
    }
    if(x1<0 || x2<0 || y1<0 || y2<0){
        return false;
    }
    if(!Number.isInteger(x1) || !Number.isInteger(x2) || !Number.isInteger(y1) || !Number.isInteger(y2)){
        return false;
    }
    return true;

});

const randomNum=Math.floor((Math.random()*100) + 1);
const randomNegNum=Math.floor(((Math.random()*100) + 1)*-1);
const x1IsNull = mockFn(randomNum,3,2,3);
const stringInput="String"


test("Create task Form validation with null values ",()=>{

    expect(mockFn(null,randomNum,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,null,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,null,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,randomNum+2,null)).toBeFalsy()
    expect(mockFn(randomNegNum,randomNum,randomNum+1,randomNum+2)).toBeFalsy()


})
test("Create task Form validation with null values ",()=>{
    expect(mockFn(randomNegNum,randomNum,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNegNum,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,randomNegNum,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,randomNum+2,randomNegNum)).toBeFalsy()
})

test("Create Task Form validation with String values",()=>{

    expect(mockFn(stringInput,randomNum,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,stringInput,randomNum+1,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,stringInput,randomNum+2)).toBeFalsy()
    expect(mockFn(randomNum,randomNum+1,randomNum+2,stringInput)).toBeFalsy()

})
test("Create Task Form validation with Valid Input",()=>{

    expect(mockFn(randomNum+3,randomNum,randomNum+1,randomNum+2)).toBeTruthy()

})



