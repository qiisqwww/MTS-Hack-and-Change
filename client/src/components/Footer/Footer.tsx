import styles from "./Footer.module.css";
import ChillGuy from "../../assets/ChillGuys.svg";

export default function Footer() {
  return (
    <footer className={styles.footer}>
      <div className={styles.contacts}>
        <p>
          MVP сервис разработанный командой ChillGuys для трека "Web/DA: Сервис
          визуализации организационной структуры от МТС" от хакатона "Hack &
          Change от Changellenge". Символика была взята с сайта moskva.mts.ru
        </p>
        <p>©ChillGuys, 2024</p>
      </div>
      <div className={styles.chillSection}>
        <p className={styles.chill}>
          <span className={styles.span}>МТС</span>, А ВЫ НА ЧИЛЛЕ?{" "}
        </p>
        <img src={ChillGuy} alt="ChillGuy"></img>
      </div>
    </footer>
  );
}
