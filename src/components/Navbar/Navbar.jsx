import { useState } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import Main from "./nav";


const Navbar = () => {
   const [activeNavItem, setActiveNavItem] = useState("home"); // Set the default active item here

   // Event handler to update the active navbar item when clicked
   const handleNavItemClick = (navItemId) => {
    console.log(navItemId);
    setActiveNavItem(navItemId);
     
   };
  return (
    <>
      <Main />
      <button type="button" className="mobile-nav-toggle d-lg-none">
        <i className="icofont-navigation-menu"></i>
      </button>
      <header id="header" className="fixed-top ">
        <div className="container-fluid navbur">
          <div className="navi">
            <div className="col-xl-12 d-flex align-items-center lefty">
              <h5 className="ld-flex mr-auto devman">
                {/* <img
                  src="https://code.google.com/images/developers.png"
                  alt=""
                /> */}
                Full Stack Developer
                <span className="blink"> _ </span>
              </h5>
              <nav className="nav-menu  mainMenu">
                <ul>
                  <li
                    onClick={() => handleNavItemClick("home")}
                    className={activeNavItem === "home" ? "active" : ""}
                    data-aos-duration="300"
                  >
                    <a href="#home">Home</a>
                  </li>
                  <li
                    onClick={() => handleNavItemClick("about")}
                    className={activeNavItem === "about" ? "active" : ""}
                    data-aos-duration="200"
                  >
                    <a href="#about">About</a>
                  </li>
                  <li
                    onClick={() => handleNavItemClick("services")}
                    className={activeNavItem === "services" ? "active" : ""}
                    data-aos-duration="900"
                  >
                    <a href="#services">Services</a>
                  </li>
                  <li
                    onClick={() => handleNavItemClick("skills")}
                    className={activeNavItem === "skills" ? "active" : ""}
                    data-aos-duration="1200"
                  >
                    <a href="#skills">Skills</a>
                  </li>
                  <li
                    onClick={() => handleNavItemClick("work")}
                    className={activeNavItem === "work" ? "active" : ""}
                    data-aos-duration="1500"
                  >
                    <a href="#work">projects</a>
                  </li>
                  <li
                    onClick={() => handleNavItemClick("contact")}
                    className={activeNavItem === "contact" ? "active" : ""}
                    data-aos-duration="1900"
                  >
                    <a href="#contact">contact</a>
                  </li>
                </ul>
              </nav>
              <div className="nav-social">
                <i className="fa fa-github"></i>
              </div>
              <div className="left-btns">
                <div id="theme-button2">
                  <input id="toggle" class="toggle" type="checkbox"></input>
                </div>
                <div>
                  <div className="CvMe">
                    <button className="my-cv">Contact Me</button>
                  </div>
                </div>

                <div className=" " id="theme-button">
                  <Link to="#" class="menuBtn">
                    <span class="lines"></span>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </>
  );
};

export default Navbar;
