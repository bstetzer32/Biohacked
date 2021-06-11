import React, { useEffect, useState } from "react";
import ReactHlsPlayer from 'react-hls-player';
import { useDispatch, useSelector } from "react-redux";
import { Card, CardActions, Typography, CardContent, Button, Modal, CardMedia } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';

import {getExcercise} from '../store/exercises'

const useStyles = makeStyles((theme) => ({
    modal: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center",
        marginTop: "10%",
        maxHeight: "80%"
    },
    card: {
        width: "80%",
        overflow: "scroll"
    }
}))

export default function ExerciseModal({id, api_id}) {
    const exercises = useSelector(state=>state.exercises)
    const exercise = exercises[id]
    const [open, setOpen] = useState(false);
    const dispatch = useDispatch()
    const classes = useStyles()

    const handleOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
    };
    const getInfo = (e) => {
        e.preventDefault()
        if (!exercise) {
            dispatch(getExcercise(id, api_id)).then(
                ()=>{
                    handleOpen()
                }
            )     
            } else {
                handleOpen()
            }
    }


    return (
        <>
            <Button onClick={getInfo}>
                {`Media & Instructions`}
            </Button>
            <Modal className={classes.modal} open={open} onClose={handleClose}>
                <Card className={classes.card}>
                {exercise ? <>
                        {exercise.video ?
                            <ReactHlsPlayer
                                src={exercise.video}
                                autoPlay={false}
                                controls={true}
                                width="100%"
                                height="auto"
                            /> 
                            : <CardMedia component="img" src={exercise.image}/>}
                        <CardContent>
                            <Typography variant="h4">
                                {exercise.name}
                            </Typography>
                            <Typography variant="h6">
                                Target Muscle: 
                            </Typography>
                            <Typography variant="subtitle1">
                                {exercise.target_muscle}
                            </Typography>
                            <Typography variant="h6">
                                Preparation:
                            </Typography>
                            <Typography variant="subtitle1">
                                {exercise.preparation}
                            </Typography>
                            <Typography variant="h6">
                                Execution:
                            </Typography>
                            <Typography variant="subtitle1">
                                {exercise.execution}
                            </Typography>
                        </CardContent></>
                    :
                    <Card>
                        Loading..
                    </Card>
                }
                </Card>
            </Modal>
        </>
    )
}