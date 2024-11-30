import Arrow from "../Arrow/Arrow";
import styles from "./Filter.module.css";

interface FilterProps {
  title: string;
}
export default function Filter({ title }: FilterProps) {
  return (
    <li className={styles.filter}>
      <div className={styles.section}>
        <h2 className={styles.title}>{title}</h2>
        <Arrow />
      </div>
      {/* <input type="checkbox" pattern="check" /> */}
    </li>
  );
}
