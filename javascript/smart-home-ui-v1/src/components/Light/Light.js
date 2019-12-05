import React, { useState, useEffect } from 'react'
import {GiCeilingLight} from 'react-icons/gi';


const Light = (props) => {
    const {url, sensorName} = props
    const [fillColour, setFillColour] = useState("white")
    const fetchConfig = {
        headers: {"Content-Type": "application/json"}, method: "GET"
    }

    const doGet = () => {
        fetch(url, fetchConfig)
            .then(res => res.json())
            .then(data => {
                let isOn = (data[sensorName] === "ON")
                let isOff = (data[sensorName] === "OFF")
                if ( isOn && fillColour === "white"){
                    setFillColour("yellow")
                }
                if (isOff && fillColour === "yellow") {
                    setFillColour("white")
                }
            })
            .catch(error => console.log(error));
    }

    useEffect(() => {
        const intervalId = setInterval(() => { doGet() }, 5000)
		return () => clearInterval(intervalId)
      }, [fillColour]);

    return(
        <button className="btn">
            <GiCeilingLight style={{fill: fillColour , height: "60px", width: "60px"}} stroke="black" strokeWidth="5px"/>
        </button>
    )
}
export default Light