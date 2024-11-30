import styles from "./Input.module.css";

interface InputProps {
  isSearch: boolean;
  setIsSearch: React.Dispatch<React.SetStateAction<boolean>>;
}

export default function Input({ isSearch, setIsSearch }: InputProps) {
  const handleSearch = () => {
    setIsSearch(true);
  };

  return (
    <div
      className={`${styles.border} ${isSearch ? styles.borderOnSearch : " "}`}
    >
      <input
        placeholder="Поиск сотрудника"
        className={`${styles.input} ${isSearch ? styles.inputOnSearch : " "}`}
      ></input>
      <div className={styles.bottom}>
        <button className={styles.button}>
          <svg
            width="24"
            height="24"
            viewBox="0 0 24 24"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M9 7C9 4.23858 11.2386 2 14 2C16.7614 2 19 4.23858 19 7V15C19 18.866 15.866 22 12 22C8.13401 22 5 18.866 5 15V9C5 8.44772 5.44772 8 6 8C6.55228 8 7 8.44772 7 9V15C7 17.7614 9.23858 20 12 20C14.7614 20 17 17.7614 17 15V7C17 5.34315 15.6569 4 14 4C12.3431 4 11 5.34315 11 7V15C11 15.5523 11.4477 16 12 16C12.5523 16 13 15.5523 13 15V9C13 8.44772 13.4477 8 14 8C14.5523 8 15 8.44772 15 9V15C15 16.6569 13.6569 18 12 18C10.3431 18 9 16.6569 9 15V7Z"
              fill="#969FA8"
            />
          </svg>
        </button>
        <button
          className={`${styles.button} ${styles.submit} ${
            isSearch ? styles.submitPushed : ""
          }`}
          onClick={handleSearch}
        >
          <svg
            width="14"
            height="16"
            viewBox="0 0 14 16"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              clip-rule="evenodd"
              d="M6.1918 0.906029C6.6381 0.459709 7.3618 0.459709 7.8081 0.906029L12.9509 6.04888C13.3972 6.49518 13.3972 7.21878 12.9509 7.66508C12.5046 8.11148 11.781 8.11148 11.3347 7.66508L8.1428 4.47328V14.2856C8.1428 14.9168 7.6311 15.4285 6.9999 15.4285C6.3688 15.4285 5.8571 14.9168 5.8571 14.2856V4.47328L2.6652 7.66508C2.2189 8.11148 1.4953 8.11148 1.049 7.66508C0.602646 7.21878 0.602646 6.49518 1.049 6.04888L6.1918 0.906029Z"
              fill="white"
            />
          </svg>
        </button>
      </div>
    </div>
  );
}
