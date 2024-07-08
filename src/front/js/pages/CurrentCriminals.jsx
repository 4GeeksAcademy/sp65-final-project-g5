import React, { useContext, useEffect, useState } from "react";
import "../../styles/index.css";
import "../../styles/cards.css";
import { Link, useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import freddy from "../../img/freddykrueger.jpg";
import hannibal from "../../img/hannibal.webp";
import jason from "../../img/jason.webp";
import psycho from "../../img/psycho.png";
import dahmer from "../../img/dahmer.jpeg";
import missery from "../../img/Missery.jpeg";
import ma from "../../img/ma.png";
import monster from "../../img/monster.png";
import tiffany from "../../img/tiffany.png";
import karla from "../../img/karla.png";
import bundy from "../../img/bundy.jpeg";
import american from "../../img/american.png";

export const CurrentCriminal = () => {
    const { store, actions } = useContext(Context);
    const [comment, setComment] = useState();
    const avatars = [freddy, missery, hannibal, jason, karla, psycho, tiffany, american, monster, ma, dahmer, bundy];

    useEffect(() => {
        actions.getCurrentCriminal()
        actions.getCurrentCriminalComments()
        actions.addCommentCriminal()
    }, [])

    const handleSubmit = () => {

        if (comment.trim !== '') {
            const dataToSend = {
                user_id: store.user.id,
                criminal_id: store.currentCriminalId,
                comment: comment,
                comment_date: new Date()
            }
            actions.addCommentCriminal(dataToSend)
            setComment('')
        }
    }

    return (
        <div className="p-5 justify-content-center bg-dark">
            {!store.currentCriminal ? <p>Not found</p> :
                <div className="card mb-3 bg-primary">
                    <div className="text-end mt-2">
                        <Link to="/criminals">
                            <i className="fas fa-times close fa-xl sing-close"></i>
                        </Link>
                    </div>
                    <div className="row g-0 p-5">
                        <div className="col-3 mb-5 current-card border-none">
                            <img src={store.currentCriminal.images} className="img-fluid" alt="..." />
                            <h4 className="mt-3 text-center title"> aliases: </h4>
                            <p calssName=" body">{store.currentCriminal.aliases ? store.currentCriminal.aliases.replace(/['"\[\]]/g, '') : ''}</p>
                        </div>
                        <div className="col-md-6 ms-5">
                            <div className="card-body text-light">
                                <div className='mb-5'>
                                    <h1 className="card-title title"> {store.currentCriminal.title} </h1>
                                    <p>{store.currentCriminal.subjects ? store.currentCriminal.subjects.replace(/['"\[\]]/g, '') : ''}</p>
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.dates_of_birth_used == null || store.currentCriminal.dates_of_birth_used == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Date of birth used:</span> {store.currentCriminal.dates_of_birth_used.replace(/['"\[\]]/g, '')}  </p>}
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.nationality == null || store.currentCriminal.nationality == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Nationality: </span> {store.currentCriminal.nationality} </p>
                                    }
                                </div>
                                <div>
                                    {store.currentCriminal.place_of_birth == null || store.currentCriminal.place_of_birth == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Place of birth: </span> {store.currentCriminal.place_of_birth} </p>
                                    }
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.sex == null || store.currentCriminal.sex == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Sex: </span> {store.currentCriminal.sex}</p>
                                    }
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.hair_raw == null || store.currentCriminal.hair_raw == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Hair: </span> {store.currentCriminal.hair_raw} </p>
                                    }
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.remarks == null || store.currentCriminal.remarks == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Remarks: </span> {store.currentCriminal.remarks.replace(/\[|\]|<p>|<\/p>/g, '')} </p>
                                    }
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.field_offices == null || store.currentCriminal.field_offices == 'None' ? ''
                                        :
                                        <p className="card-text mt-1 body"> <span className="title">Field offices: </span> {store.currentCriminal.field_offices.replace(/['"\[\]]/g, '')}  </p>
                                    }
                                </div>
                                <div className="mb-1">
                                    {store.currentCriminal.caution == null || store.currentCriminal.caution == 'None' ? ''
                                        :
                                        <p className="card-text body"> <span className="title">Caution: </span> {store.currentCriminal.caution.replace(/\[|\]|<p>|<\/p>/g, '')}  </p>
                                    }
                                </div>
                            </div>
                        </div>
                        <div className="d-flex justify-content-end mb-5">
                            {store.isLogin ?
                                <Link to="/create-story" className="btn btn-outline-light ms-3 body">Create your Storie</Link>
                                : ''
                            }

                        </div>
                        <div className='mb-2'>
                            {store.currentCriminalComments == '' ? '' : <h1 className="title text-light"> Comments </h1>}
                        </div>
                        {store.currentCriminalComments.map((item, id) =>
                            <div key={id} className="card">
                                <div className="row mt-4">
                                    <div className=" col-1 avatar-comment ms-3 d-flex justify-content-end ">
                                        <img src={avatars[item.user.avatar]} alt="mdo" className="rounded-circle" />
                                    </div>
                                    <div className="col-9 card-body p-none aling-text-start user-comment mt-1 mb-3 title me-5">
                                        {item.user.name} {item.user.surname} <p className="body">
                                            {item.comment} </p>
                                    </div>
                                </div>
                            </div>
                        )}

                        {store.isLogin ?
                            <div>
                                <div className="mb-3 mt-3 justify-content-end">
                                    <label htmlFor="exampleFormControlTextarea1" className="form-label text-light"> Write your comment here</label>
                                    <textarea className="form-control" id="exampleFormControlTextarea1" rows="3" value={comment} onChange={(event) => setComment(event.target.value)}></textarea>
                                </div>
                                <button type="submit" className="btn btn-outline-light mt-3 body" onClick={() => handleSubmit()}>Comment</button>
                            </div>
                            : ''
                        }
                    </div>
                </div>
            }
        </div >
    );
};