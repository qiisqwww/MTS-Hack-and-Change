import styles from "./Card.module.css";
import defaultAvatar from "../../assets/defaultAvatar.svg";
import { IPreson } from "../../interfaces/IPerson";
import dayjs from "dayjs";
import axios, { AxiosError } from "axios";
import { useCards } from "../../context/DataContext";

interface CardProps {
  setPopup: React.Dispatch<React.SetStateAction<boolean>>;
  card: IPreson;
}

export default function Card({ setPopup, card }: CardProps) {
  const { setMaster, setCards } = useCards();
  const currentDate = dayjs();
  const age = currentDate.diff(card.birthdate, "year");

  const handleMaster = async () => {
    try {
      const response = await axios.get<IPreson>(
        `${import.meta.env.VITE_API_URL}/boss`,
        {
          params: {
            boss_id: card.boss_id,
          },
        }
      );
      setMaster(response.data);
    } catch (error: unknown) {
      const e = error as AxiosError;
      console.error(e);
    }
  };

  const handleSub = async () => {
    try {
      const response = await axios.get<IPreson[]>(
        `${import.meta.env.VITE_API_URL}/subs`,
        {
          params: {
            boss_id: card.id,
          },
        }
      );
      console.log(response.data);
      setCards(response.data);
    } catch (error: unknown) {
      const e = error as AxiosError;
      console.error(e);
    }
  };

  const handleMore = async () => {
    try {
      const response = await axios.get<IPreson>(
        `${import.meta.env.VITE_API_URL}/boss`,
        {
          params: {
            boss_id: card.id,
          },
        }
      );
      setMaster(response.data);
    } catch (error: unknown) {
      const e = error as AxiosError;
      console.error(e);
    }
  };

  return (
    <div className={styles.card}>
      <div className={styles.displayFlex}>
        <img src={defaultAvatar} alt="avatar" className={styles.icon}></img>
        <div>
          <h2 className={styles.name}>
            {card.first_name} {card.last_name}
          </h2>
          <h3 className={styles.age}>
            {age} y.o
            {card.on_sick_leave_info ? (
              <li className={styles.sick}>
                <span>
                  On sick leave from {String(card.on_sick_leave_info.date_from)} to{" "}
                  {String(card.on_sick_leave_info.date_to)}
                </span>
              </li>
            ) : (
              " "
            )}
            {card.on_leave_info ? (
              <li className={styles.sick}>
                <span>
                  On leave from {String(card.on_leave_info.date_from)} to{" "}
                  {String(card.on_leave_info.date_to)}
                </span>
              </li>
            ) : (
              " "
            )}
          </h3>
          <div className={styles.displayFlex}>
            <div className={styles.job}>
              <p>{card.post}</p>
            </div>
            <div className={styles.role}>
              <p>{card.role}</p>
            </div>
          </div>
        </div>
        <button
          className={styles.button}
          onClick={() => {
            handleMore();
            setPopup(true);
          }}
        >
          MORE
        </button>
      </div>
      <div>
        <div className={styles.grid}>
          <h4 className={styles.point}>Contact</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>{card.phone_number}</p>
            <p className={styles.text}>{card.email}</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Dep.</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>{card.department_name}</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Func. bloc</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>Corp. block</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid}>
          <h4 className={styles.point}>Address</h4>
          <div className={styles.displayFlex}>
            <p className={styles.text}>{card.address}</p>
          </div>
        </div>
        <hr className={styles.line}></hr>
        <div className={styles.grid + " " + styles.team}>
          {card.boss_id && (
            <button
              className={styles.point + " " + styles.master}
              onClick={() => {
                handleMaster();
                setPopup(true);
              }}
            >
              Header
            </button>
          )}

          <button
            className={styles.point + " " + styles.master}
            onClick={() => {
              handleSub();
            }}
          >
            Staff
          </button>
        </div>
        {/* <hr className={styles.line}></hr>/ */}
      </div>
    </div>
  );
}
