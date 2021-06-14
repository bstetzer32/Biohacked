import React from "react";
import {  useSelector } from "react-redux";
// import {Link} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardActions, Typography } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
// import CardMedia from '@material-ui/core/CardMedia';
// import Button from '@material-ui/core/Button';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faDumbbell } from '@fortawesome/free-solid-svg-icons'
import ExerciseModal from './ExerciseModal'

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
        flexDirection: "column",
        height: "100%",
        width: "80%",
        margin: "2.5%",
        padding: "2.5%"
    },
    content : {
        display: "flex",
        justifyContent: "space-between"
    },
    form: {
        display: "flex",
        justifyContent: "space-between",
    },
    formEl: {
        margin: "5%",
        minWidth: "5%"
    },
    decorator: {
        [theme.breakpoints.down('sm')]: {
        display: "none"
        }
    }
}))

export default function ResultTile({exercise}) {
    const res = useSelector(state=>state.results[exercise.id])
    const results = {...res?.results}
    // console.log(results)
    const classes = useStyles()
    const scheme = exercise.scheme
    let sets =  exercise.sets
    
    return (
        <Card className={classes.root}>
            <CardContent className={classes.content}>
                <div>
                <Typography variant="h6">
                    {exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(0,1).toUpperCase()}{exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(1)} {exercise.movement}
                </Typography>
                
                <ExerciseModal id={exercise.id} api_id={exercise.api_id}/>
                </div>
            </CardContent>
                {((scheme.name.includes('Compound') || scheme.name.includes('Isolated')) && sets) ? sets.map((set, i) =>{
                    return (<div className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>Set: {set.set}</Typography>
                                <Typography className={classes.formEl}>Reps: {set.reps}</Typography>
                                <Typography className={classes.formEl}>Load: {set.load}lbs</Typography>
                                <Typography className={classes.formEl}>Rest: {set.rest}sec</Typography>
                        </div>)
                }): ((scheme.name.includes('Stretch') || scheme.name.includes('Static')|| scheme.name.includes('TABATA')) && sets) ? sets.map((set, i) =>{
                    return (<div className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>Set: {set.set}</Typography>
                                <Typography className={classes.formEl}>Work: {set.work}sec</Typography>
                                <Typography className={classes.formEl}>Rest: {set.rest}sec</Typography>
                        </div>)}):((scheme.name.includes('Warmup') || scheme.name.includes('Dynamic')) && sets)? sets.map((set, i) =>{
                    return (<div className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>Set: {set.set}</Typography>
                                <Typography className={classes.formEl}>Reps: {set.reps}</Typography>
                                <Typography className={classes.formEl}>Rest: {set.rest}sec</Typography>
                        </div>)}) : sets? exercise.sets.map((set, i) =>{
                    return (<div className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>Set: {set.set}</Typography>
                                <Typography className={classes.formEl}>Work: {set.work}</Typography>

                        </div>)}) : null}
            <CardActions>
            </CardActions>
        </Card>
    )
}