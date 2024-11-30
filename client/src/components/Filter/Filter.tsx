import { Select } from "antd";
import Arrow from "../Arrow/Arrow";
import styles from "./Filter.module.css";

interface FilterProps {
  title: string;
  isList: boolean;
}
export default function Filter({ title, isList }: FilterProps) {
  return (
    <li className={styles.filter}>
      <div className={styles.section}>
        <h2 className={styles.title}>{title}</h2>
        <Arrow />
      </div>
      {isList ? (
        <Select
          showSearch
          className={styles.select}
          placeholder="Select"
          optionFilterProp="label"
          options={[
            {
              value: "jack",
              label: "Jack",
            },
            {
              value: "lucy",
              label: "Lucy",
            },
            {
              value: "tom",
              label: "Tom",
            },
          ]}
        />
      ) : (
        <input className={styles.input} />
      )}
    </li>
  );
}
