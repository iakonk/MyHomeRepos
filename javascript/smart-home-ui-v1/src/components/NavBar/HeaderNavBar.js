import React from 'react';

const HeaderNavBar = () => {
    return (
        <header className="topbar" data-navbarbg="skin5">
            <nav className="navbar top-navbar navbar-expand-md navbar-dark">
                <div className="navbar-header" data-logobg="skin5">
                    <a className="nav-toggler waves-effect waves-light d-block d-md-none" href="javascript:void(0)"><i className="ti-menu ti-close"></i></a>
                    <a className="navbar-brand" href="index.html">
                        <b className="logo-icon p-l-10">
                            <img src="assets/images/logo-icon.png" alt="homepage" className="light-logo img-fluid" />
                        </b>
                        <span className="logo-text">Smart House Admin</span>
                    </a>
                    <a className="topbartoggler d-block d-md-none waves-effect waves-light" href="javascript:void(0)" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><i className="ti-more"></i></a>
                </div>
                <div className="navbar-collapse collapse" id="navbarSupportedContent" data-navbarbg="skin5">
                    <ul className="navbar-nav float-left mr-auto">
                        <li className="nav-item d-none d-md-block"><a className="nav-link sidebartoggler waves-effect waves-light" href="javascript:void(0)" data-sidebartype="mini-sidebar"><i className="mdi mdi-menu font-24"></i></a></li>
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                             <span className="d-none d-md-block">Create New <i className="fa fa-angle-down"></i></span>
                             <span className="d-block d-md-none"><i className="fa fa-plus"></i></span>
                            </a>
                            <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                <a className="dropdown-item" href="#">Action</a>
                                <a className="dropdown-item" href="#">Another action</a>
                                <div className="dropdown-divider"></div>
                                <a className="dropdown-item" href="#">Something else here</a>
                            </div>
                        </li>
                        <li className="nav-item search-box"> <a className="nav-link waves-effect waves-dark" href="javascript:void(0)"><i className="ti-search"></i></a>
                            <form className="app-search position-absolute">
                                <input type="text" className="form-control" placeholder="Search &amp; enter" /> <a className="srh-btn"><i className="ti-close"></i></a>
                            </form>
                        </li>
                    </ul>
                    <ul className="navbar-nav float-right">
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle waves-effect waves-dark" href="" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> <i className="mdi mdi-bell font-24"></i>
                            </a>
                             <div className="dropdown-menu" aria-labelledby="navbarDropdown">
                                <a className="dropdown-item" href="#">Action</a>
                                <a className="dropdown-item" href="#">Another action</a>
                                <div className="dropdown-divider"></div>
                                <a className="dropdown-item" href="#">Something else here</a>
                            </div>
                        </li>
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle text-muted waves-effect waves-dark pro-pic" href="" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"><img src="assets/images/users/1.jpg" alt="user" className="rounded-circle" width="31" /></a>
                            <div className="dropdown-menu dropdown-menu-right user-dd animated">
                                <a className="dropdown-item" href="javascript:void(0)"><i className="ti-user m-r-5 m-l-5"></i> My Profile</a>
                                <a className="dropdown-item" href="javascript:void(0)"><i className="ti-wallet m-r-5 m-l-5"></i> My Balance</a>
                                <a className="dropdown-item" href="javascript:void(0)"><i className="ti-email m-r-5 m-l-5"></i> Inbox</a>
                                <div className="dropdown-divider"></div>
                                <a className="dropdown-item" href="javascript:void(0)"><i className="ti-settings m-r-5 m-l-5"></i> Account Setting</a>
                                <div className="dropdown-divider"></div>
                                <a className="dropdown-item" href="javascript:void(0)"><i className="fa fa-power-off m-r-5 m-l-5"></i> Logout</a>
                                <div className="dropdown-divider"></div>
                                <div className="p-l-30 p-10"><a href="javascript:void(0)" className="btn btn-sm btn-success btn-rounded">View Profile</a></div>
                            </div>
                        </li>
                    </ul>
                </div>
            </nav>
        </header>
    )
}
export default HeaderNavBar