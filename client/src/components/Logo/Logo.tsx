import { Switch } from "antd";
import logo from "../../../public/MTC_Logo_RGB.svg";
import styles from "./Logo.module.css";
import { useTheme } from "../../hooks/useTheme";

export default function Logo() {
  const { theme, setTheme } = useTheme();
  console.log(theme);
  const toggleTheme = () => {
    setTheme(theme === "light" ? "dark" : "light");
  };

  return (
    <div className={styles.section}>
      <div className={styles.logo}>
        <img src={logo} alt="logo" className={styles.icon}></img>
        <p className={styles.text}>HACK</p>
      </div>
      <Switch
        // defaultChecked
        className={styles.customSwitch}
        onChange={toggleTheme}
      />
    </div>
  );
}
