import { motion } from "framer-motion";
import Arrow from "../Arrow/Arrow";
import styles from "./Filter.module.css";
import { useState } from "react";

interface FilterProps {
  title: string;
  isList: boolean;
  options?: { id: number; name: string }[];
  inputRef?: (el: HTMLInputElement | HTMLSelectElement | null) => void;
}

const variants = {
  open: { height: "auto", opacity: 1, margin: "0 0 20px 0" },
  closed: { height: 0, opacity: 0, margin: 0 },
};

export default function Filter({
  title,
  isList,
  options,
  inputRef,
}: FilterProps) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <li className={styles.filter}>
      <div
        className={styles.section}
        onClick={() => {
          setIsOpen(!isOpen);
        }}
      >
        <h2 className={styles.title}>{title}</h2>
        <div className={`${styles.arrow} ${isOpen ? styles.rotate : " "}`}>
          <Arrow />
        </div>
      </div>
      <motion.div
        initial={false}
        transition={{
          duration: 0.3,
        }}
        animate={isOpen ? "open" : "closed"}
        variants={variants}
        className={styles.text}
      >
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
      </motion.div>
    </li>
  );
}
