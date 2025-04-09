import styles from "./Footer.module.css";
import ChillGuy from "../../assets/ChillGuys.svg";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.contacts}>
        <p>
            MVP is a service developed by the ChillGuys team for the track "Web/DA: Service
            visualizations of the organizational structure from MTS" from the hackathon "Hack &
            Change from Changellenge". The symbols were taken from the website moskva.mts.ru
        </p>
        <p>©ChillGuys, 2024</p>
      </div>
      <div className={styles.chillSection}>
        <p className={styles.chill}>
          <span className={styles.span}>МТС</span>, А ВЫ НА ЧИЛЛЕ?{" "}
        </p>
        <img src={ChillGuy} alt="ChillGuy" className={styles.icon}></img>
      </div>
    </footer>
  );
}
