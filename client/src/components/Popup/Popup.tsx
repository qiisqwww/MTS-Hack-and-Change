import styles from "./Popup.module.css";
import defaultAvatar from "../../assets/defaultAvatar.svg";
import Cross from "../../assets/Cross.svg";
import { ForwardedRef, forwardRef, useEffect, useState } from "react";
import { motion } from "motion/react";
import { useCards } from "../../context/DataContext";
import dayjs from "dayjs";
import axios, { AxiosError } from "axios";
import { IPreson } from "../../interfaces/IPerson";

interface PopupProps {
  setPopup: React.Dispatch<React.SetStateAction<boolean>>;
}

export const Popup = forwardRef(
  ({ setPopup }: PopupProps, ref: ForwardedRef<HTMLDivElement>) => {
    const [age, setAge] = useState<number | null>(null);
    const { master, setMaster } = useCards();
    useEffect(() => {
      const currentDate = dayjs();
      const age = currentDate.diff(master?.birthdate, "year");
      setAge(age);
    }, [master]);
    const handleMaster = async () => {
      try {
        const response = await axios.get<IPreson>(
          `${import.meta.env.VITE_API_URL}/boss`,
          {
            params: {
              boss_id: master?.boss_id,
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
      <div className={styles.backgroundPopup} ref={ref}>
        <div className={styles.card}>
          <div className={styles.displayFlex}>
            <img src={defaultAvatar} alt="avatar" className={styles.icon}></img>
            <div>
              <h2 className={styles.name}>
                {master?.first_name} {master?.last_name}
              </h2>
              <h3 className={styles.age}>
                {age} года{" "}
                {master?.on_sick_leave_info ? (
                  <li className={styles.sick}>
                    <span>
                      On sick leave{" "}
                      {String(master?.on_sick_leave_info.date_from)} from{" "}
                      {String(master?.on_sick_leave_info.date_to)}
                    </span>
                  </li>
                ) : (
                  " "
                )}
                {master?.on_leave_info ? (
                  <li className={styles.sick}>
                    <span>
                      On leave {String(master?.on_leave_info.date_from)} to{" "}
                      {String(master?.on_leave_info.date_to)}
                    </span>
                  </li>
                ) : (
                  " "
                )}
              </h3>
              <div className={styles.displayFlex}>
                <div className={styles.job}>
                  <p>{master?.post}</p>
                </div>
                <div className={styles.role}>
                  <p>{master?.role}</p>
                </div>
              </div>
            </div>
            <button
              className={styles.button}
              onClick={() => {
                setPopup(false);
              }}
            >
              <img src={Cross} alt="cross" />
            </button>
          </div>
          <div>
            <div className={styles.grid}>
              <h4 className={styles.point}>Phone</h4>
              <div className={styles.displayFlex}>
                <p className={styles.text}>{master?.phone_number}</p>
                <p className={styles.text}>{master?.email}</p>
              </div>
            </div>
            <hr className={styles.line}></hr>
            <div className={styles.grid}>
              <h4 className={styles.point}>Department</h4>
              <div className={styles.displayFlex}>
                <p className={styles.text}>{master?.department_name}</p>
              </div>
            </div>
            <hr className={styles.line}></hr>
            <div className={styles.grid}>
              <h4 className={styles.point}>Func. block</h4>
              <div className={styles.displayFlex}>
                <p className={styles.text}>Corp. block</p>
              </div>
            </div>
            <hr className={styles.line}></hr>
            <div className={styles.grid}>
              <h4 className={styles.point}>Address</h4>
              <div className={styles.displayFlex}>
                <p className={styles.text}>{master?.address}</p>
              </div>
            </div>

            <hr className={styles.line}></hr>
            <div className={styles.grid}>
              <h4 className={styles.point}>About</h4>
              <div className={styles.displayFlex}>
                <p className={styles.text}>
                  Chill guy — likes not to sleep for two days because of the hackathon,
                  Because he's a chill guy, likes to go out and hang out with
                  friends.
                </p>
              </div>
            </div>
            <hr className={styles.line}></hr>
            {master?.boss_id && (
              <button
                className={styles.point + " " + styles.master}
                onClick={() => {
                  handleMaster();
                }}
              >
                Header
              </button>
            )}
          </div>
        </div>
      </div>
    );
  }
);

export const MPopup = motion(Popup);
