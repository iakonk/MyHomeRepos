import React, {Component} from 'react';
import HeaderNavBar from '../NavBar/HeaderNavBar';
import SideNavBar from '../NavBar/SideNavBar';

const Layout = ({children}) => {
    return(
            <div>
                <HeaderNavBar />
                <SideNavBar />
                <div className="page-wrapper">
                     <div className="page-breadcrumb">
                        <div className="row">
                            <div className="col-12 d-flex no-block align-items-center">
                                <h4 className="page-title">Dashboard</h4>
                            </div>
                        </div>
                     </div>
                    <div className="container-fluid">
                       {children}
                    </div>
                    <footer className="footer text-center"><i className="far fa-copyright"><span> All rights reserved</span></i></footer>
                </div>
           </div>
    )
 }

export default Layout
