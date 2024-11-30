import { Switch } from "antd";
import logo from "../../../public/MTC_Logo_RGB.svg";
import styles from "./Logo.module.css";
import { useState } from "react";

export default function Logo() {
  const [theme, setTheme] = useState("light");
  console.log(theme);
  return (
    <div className={styles.section}>
      <div className={styles.logo}>
        <img src={logo} alt="logo" className={styles.icon}></img>
        <p className={styles.text}>HACK</p>
      </div>
      <Switch
        // defaultChecked
        className={styles.customSwitch}
        onChange={() => {
          setTheme("dark");
        }}
      />
    </div>
  );
}
