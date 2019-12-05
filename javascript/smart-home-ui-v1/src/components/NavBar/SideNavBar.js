import React, {useState, useEffect} from 'react';
import { NavLink, HashRouter } from 'react-router-dom';

const selectedStyle = {
    className: "sidebar-link waves-effect waves-dark sidebar-link active"
}

const SideNavBar = () => {
  const [selectedId, setSelectedId] = useState("Dashboard")

  const changeSelected = (e) => {
       let currentSelectedElem = document.getElementById(selectedId)
       let selected = (currentSelectedElem.classList.value.includes("selected") && e.target.innerText === selectedId)
       if (!selected){
           currentSelectedElem.classList.remove("selected")
           setSelectedId(e.target.innerText)
       }
  }

  useEffect(() => {
       let newSelectedElem = document.getElementById(selectedId)
       if (newSelectedElem){
        newSelectedElem.classList.add("selected")
       }
  }, [selectedId]);

  return (
     <HashRouter>
        <aside className="left-sidebar" data-sidebarbg="skin5">
            <div className="scroll-sidebar">
                <nav className="sidebar-nav">
                    <ul id="sidebarnav" className="p-t-30">
                        <li className="sidebar-item" id="Dashboard">
                            <NavLink to="/dashboard" className="sidebar-link waves-effect waves-dark sidebar-link"
                                    aria-expanded="false"
                                    activeStyle={selectedStyle}
                                    onClick={changeSelected}>
                                <i className="mdi mdi-view-dashboard"></i><span className="hide-menu">Dashboard</span>
                            </NavLink>
                         </li>
                        <li className="sidebar-item" id="Charts">
                             <NavLink to="/charts" className="sidebar-link waves-effect waves-dark sidebar-link"
                                    aria-expanded="false"
                                    activeStyle={selectedStyle}
                                    onClick={changeSelected}>
                                <i className="mdi mdi-chart-bar"></i><span className="hide-menu">Charts</span>
                            </NavLink>
                        </li>
                        <li className="sidebar-item">
                                <NavLink to="/charts" className="sidebar-link waves-effect waves-dark sidebar-link"
                                    aria-expanded="false"
                                    activeStyle={selectedStyle}
                                    onClick={changeSelected}>
                                <i className="mdi mdi-chart-bar"></i><span className="hide-menu">Weather</span>
                            </NavLink>
                         <a className="sidebar-link waves-effect waves-dark sidebar-link" href="widgets.html" aria-expanded="false">
                         <i className="mdi mdi-weather-partlycloudy"></i><span className="hide-menu">Weather</span></a>
                        </li>
                        <li className="sidebar-item"> <a className="sidebar-link waves-effect waves-dark sidebar-link" href="tables.html" aria-expanded="false"><i className="mdi mdi-bell-ring-outline"></i><span className="hide-menu">Door events</span></a></li>
                        <li className="sidebar-item"> <a className="sidebar-link waves-effect waves-dark sidebar-link" href="grid.html" aria-expanded="false"><i className="mdi mdi-alarm-multiple"></i><span className="hide-menu">Alarms</span></a></li>
                        <li className="sidebar-item"> <a className="sidebar-link waves-effect waves-dark sidebar-link" href="" aria-expanded="false"><i className="mdi mdi-water-pump"></i><span className="hide-menu">Water usage</span></a></li>
                        <li className="sidebar-item"> <a className="sidebar-link has-arrow waves-effect waves-dark" href="javascript:void(0)" aria-expanded="false"><i className="mdi mdi-account-key"></i><span className="hide-menu">Authentication </span></a>
                            <ul aria-expanded="false" className="collapse  first-level">
                                <li className="sidebar-item"><a href="authentication-login.html" className="sidebar-link"><i className="mdi mdi-all-inclusive"></i><span className="hide-menu"> Login </span></a></li>
                                <li className="sidebar-item"><a href="authentication-register.html" className="sidebar-link"><i className="mdi mdi-all-inclusive"></i><span className="hide-menu"> Register </span></a></li>
                            </ul>
                        </li>
                    </ul>
                </nav>
            </div>
        </aside>
     </HashRouter>
    )
}
export default SideNavBar