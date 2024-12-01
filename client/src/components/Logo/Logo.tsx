import logo from "../../../public/MTC_Logo_RGB.svg";
import styles from "./Logo.module.css";

export default function Logo() {
  return (
    <div className={styles.section}>
      <div className={styles.logo}>
        <img src={logo} alt="logo" className={styles.icon}></img>
        <p className={styles.text}>HACK</p>
      </div>
    </div>
  );
}
