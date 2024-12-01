import Arrow from "../Arrow/Arrow";
import styles from "./Filter.module.css";

interface FilterProps {
  title: string;
  isList: boolean;
  options?: { id: number; name: string }[];
  inputRef?: (el: HTMLInputElement | HTMLSelectElement | null) => void;
}

export default function Filter({
  title,
  isList,
  options,
  inputRef,
}: FilterProps) {
  return (
    <li className={styles.filter}>
      <div className={styles.section}>
        <h2 className={styles.title}>{title}</h2>
        <Arrow />
      </div>
      {isList ? (
        <select
          ref={inputRef as React.Ref<HTMLSelectElement>}
          className={styles.select}
        >
          {options?.map((option) => (
            <option key={option.id} value={option.id}>
              {option.name}
            </option>
          ))}
        </select>
      ) : (
        <input
          ref={inputRef as React.Ref<HTMLInputElement>}
          className={styles.input}
          placeholder="Введите данные"
        />
      )}
    </li>
  );
}
