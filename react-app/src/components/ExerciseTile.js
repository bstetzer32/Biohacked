import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
// import {Link} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardActions, Typography, TextField, InputAdornment, FormControl, Checkbox } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
import CardContent from '@material-ui/core/CardContent';
// import CardMedia from '@material-ui/core/CardMedia';
// import Button from '@material-ui/core/Button';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faDumbbell } from '@fortawesome/free-solid-svg-icons'
import {setResults, getResults} from '../store/results'
import ExerciseModal from './ExerciseModal'

import {getExcercise} from '../store/exercises'

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
        margin: "5%"
    }
}))

export default function ExerciseTile({exercise}) {
    const res = useSelector(state=>state.results[exercise.id])
    const dispatch = useDispatch()
    const classes = useStyles()
    const scheme = exercise.scheme
    const sets = res ? Array.from(res) : []
    useEffect(()=>{
        
    },[])

    const handleLoadChange = (e) => {
        const i = e.target.name.split('-')[e.target.name.split('-').length -1]
        // console.log(e.target)
        res[i].load = e.target.value
        dispatch(setResults({[exercise.id]: res}))
    }    
    const handleRepChange = (e) => {
        const i = e.target.name.split('-')[e.target.name.split('-').length -1]
        // console.log(e.target)
        res[i].reps = e.target.value
        dispatch(setResults({[exercise.id]: res}))
    }    
    const handleWorkChange = (e) => {
        const i = e.target.name.split('-')[e.target.name.split('-').length -1]
        // console.log(e.target)
        res[i].time = e.target.value
        dispatch(setResults({[exercise.id]: res}))
    }    
    const handleRestChange = (e) => {
        const i = e.target.name.split('-')[e.target.name.split('-').length -1]
        // console.log(e.target)
        res[i].rest = e.target.value
        dispatch(setResults({[exercise.id]: res}))
    }    
    const handleCheckedChange = (e) => {
        const i = e.target.name.split('-')[e.target.name.split('-').length -1]
        // console.log(e.target)
        res[i].checked = e.target.checked
        dispatch(setResults({[exercise.id]: res}))
    }

    useEffect(()=>{
        if (!res) {
            dispatch(getResults(exercise))
            
        }
    },[res, dispatch, exercise])

    if (!res || !sets.length) {
        return null
    }
    return (
        <Card className={classes.root}>
            <CardContent className={classes.content}>
                <div>
                <Typography variant="h6">
                    {exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(0,1).toUpperCase()}{exercise.scheme.name !== 'Core Dynamic' && exercise.movement !== 'High Intensity Interval Training' && exercise.scheme.name !== 'Warmup' && exercise.scheme.name !== 'Stretch' && exercise.modality.slice(1)} {exercise.movement}
                </Typography>
                <Typography>
                    Sets: {exercise.scheme.sets}
                </Typography>
                <Typography>
                    {exercise.scheme.reps && `Reps: ${exercise.scheme.reps}`}
                </Typography>
                <Typography>
                    {exercise.scheme.tempo && `Tempo: ${exercise.scheme.tempo}(Eccentric, Isometric, Concentric)`}
                </Typography>
                <Typography>
                    {exercise.scheme.time && `Work: ${exercise.scheme.time}s`}
                </Typography>
                <Typography>
                    {exercise.scheme.rest && `Rest: ${exercise.scheme.rest}s`}
                </Typography>
                </div>
                <ExerciseModal id={exercise.id} api_id={exercise.api_id}/>
                
            </CardContent>
            {exercise.max === 0 && (scheme.name !== 'Warmup' && scheme.name !== 'Stretch' && scheme.name !== "Cooldown" && !scheme.name.includes("Core")) &&<Typography className={classes.formEl}>Since this is your first time logging this workout, start with a weight you feel comfotable with (it's always safer to underestimate).<br/> Once you log this exercise, our algorithms will update the values for your next session.</Typography>}
                {(scheme.name.includes('Compound') || scheme.name.includes('Isolated')) ? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>{i + 1}</Typography>
                                <TextField className={classes.formEl} label="Reps" value={res[i].reps} name={`reps-${i}`} onChange={handleRepChange} InputProps={{endAdornment:<InputAdornment position="end">Reps</InputAdornment>}}/>
                                <TextField className={classes.formEl} label="Load" value={res[i].load} name={`load-${i}`} onChange={handleLoadChange} InputProps={{endAdornment:<InputAdornment position="end">Lb</InputAdornment>}}/>
                                <TextField className={classes.formEl} label="Rest" value={res[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">sec</InputAdornment>}}/>
                                <Checkbox checked={res[i].checked} onChange={handleCheckedChange} name={`checked-${i}`} color="primary"/>
                        </form>)
                }): (scheme.name.includes('Stretch') || scheme.name.includes('Static')|| scheme.name.includes('TABATA')) ? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>{i + 1}</Typography>
                                <TextField className={classes.formEl} label="Work" value={res[i].time} name={`work-${i}`} onChange={handleWorkChange} InputProps={{endAdornment:<InputAdornment position="end">sec</InputAdornment>}}/>
                                <TextField className={classes.formEl} label="Rest" value={res[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">sec</InputAdornment>}}/>
                                <Checkbox checked={res[i].checked} onChange={handleCheckedChange} name={`checked-${i}`} color="primary"/>

                        </form>)}):(scheme.name.includes('Warmup') || scheme.name.includes('Dynamic'))? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>{i + 1}</Typography>
                                <TextField className={classes.formEl} label="Reps" value={res[i].reps} name={`reps-${i}`} onChange={handleRepChange} InputProps={{endAdornment:<InputAdornment position="end">Reps</InputAdornment>}}/>
                                <TextField className={classes.formEl} label="Rest" value={res[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">sec</InputAdornment>}}/>
                                <Checkbox checked={res[i].checked} onChange={handleCheckedChange} name={`checked-${i}`} color="primary"/>

                        </form>)}) : sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                                <Typography className={classes.formEl}>{i + 1}</Typography>
                                <TextField className={classes.formEl} label="Work" value={res[i].time} name={`work-${i}`} onChange={handleWorkChange} InputProps={{endAdornment:<InputAdornment position="end">sec</InputAdornment>}}/>
                                <input type="checkbox" checked={res[i].checked} onChange={handleCheckedChange} name={`checked-${i}`} color="primary"/>

                        </form>)})}
            <CardActions>
            </CardActions>
        </Card>
    )
}