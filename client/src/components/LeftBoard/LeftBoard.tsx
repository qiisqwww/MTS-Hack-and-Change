import Filters from "../Filters/Filters";
import Logo from "../Logo/Logo";
import styles from "./LeftBoard.module.css";

export default function LeftBoard() {
  return (
    <section className={styles.section}>
      <Logo />

      <Filters />
    </section>
  );
}
