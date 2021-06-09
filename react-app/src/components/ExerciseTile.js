import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
// import {Link} from 'react-router-dom'
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardActions, Typography, TextField, InputAdornment } from '@material-ui/core';
// import CardActionArea from '@material-ui/core/CardActionArea';
// import CardContent from '@material-ui/core/CardContent';
// import CardMedia from '@material-ui/core/CardMedia';
// import Button from '@material-ui/core/Button';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
// import { faDumbbell } from '@fortawesome/free-solid-svg-icons'
import {setResults} from '../store/results'

const useStyles = makeStyles((theme) => ({
    root: {
        display: "flex",
        flexDirection: "column",
        height: "100%",
        margin: "2.5%",
        padding: "2.5%"
    },
    form: {
        display: "flex",
        justifyContent: "space-between"
    }
}))

export default function ExerciseTile({exercise}) {
    const all_results = useSelector(state=>state.results)
    const results = all_results[exercise.id]
    const dispatch = useDispatch()
    const res = {}
    const classes = useStyles()
    const scheme = exercise.scheme
    // console.log(scheme.name)
    const sets = []
    const set_reps = scheme.reps?.split(',')
    for (let i = 0; i < scheme.sets; i++) {
        if (scheme.name.includes('Compound') || scheme.name.includes('Isolated')) {
            const set = {
                reps: parseInt(set_reps[i]),
                load: Math.round((-0.0278 * exercise.max * parseInt(set_reps[i]) + 1.0278 * exercise.max)/5)*5,
                rest: scheme.rest
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Stretch') || scheme.name.includes('Static')|| scheme.name.includes('TABATA')) {
            const set = {
                time: scheme.time,
                rest: scheme.rest
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Warmup') || scheme.name.includes('Dynamic')) {
            const set = {
                reps: parseInt(set_reps[0]),
                rest: scheme.rest
            }
            sets.push(set)
            res[i] = set
        }
        if (scheme.name.includes('Cooldown')) {
            const set = {
                time: scheme.time
            }
            sets.push(set)
            res[i] = set
        }
        
    }
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

    useEffect(()=>{
        if (!results) {
            dispatch(setResults({[exercise.id]: res}))
            
        }
    },[res, dispatch, exercise.id, results])

    if (!results) {
        return null
    }
    return (
        <Card className={classes.root}>
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
            {exercise.max === 0 && (scheme.name !== 'Warmup' && scheme.name !== 'Stretch' && scheme.name !== "Cooldown" && !scheme.name.includes("Core")) &&<div>Since this is your first time logging this workout, start with a weight you feel comfotable with (it's always safer to underestimate).<br/> Once you log this exercise, our algorithms will update the values for your next session.</div>}
                {(scheme.name.includes('Compound') || scheme.name.includes('Isolated')) ? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                            <div>
                                <p>Set</p>
                                <p>{i + 1}</p>
                            </div>
                            <div>
                                <p>Reps</p>
                                <TextField label="Reps" value={results[i].reps} name={`reps-${i}`} onChange={handleRepChange} InputProps={{endAdornment:<InputAdornment position="end">Reps</InputAdornment>}}/>
                            </div>
                            <div>
                                <p>Load</p>
                                <TextField label="Load" value={results[i].load} name={`load-${i}`} onChange={handleLoadChange} InputProps={{endAdornment:<InputAdornment position="end">Lb</InputAdornment>}}/>
                            </div>
                            <div>
                                <p>Rest</p>
                                <TextField label="Rest" value={results[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">seconds</InputAdornment>}}/>
                            </div>
                        </form>)
                }): (scheme.name.includes('Stretch') || scheme.name.includes('Static')|| scheme.name.includes('TABATA')) ? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                            <div>
                                <p>Set</p>
                                <p>{i + 1}</p>
                            </div>
                            <div>
                                <p>Work</p>
                                <TextField label="Work" value={results[i].time} name={`work-${i}`} onChange={handleWorkChange} InputProps={{endAdornment:<InputAdornment position="end">seconds</InputAdornment>}}/>
                            </div>
                            <div>
                                <p>Rest</p>
                                <TextField label="Rest" value={results[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">seconds</InputAdornment>}}/>
                            </div>

                        </form>)}):(scheme.name.includes('Warmup') || scheme.name.includes('Dynamic'))? sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                            <div>
                                <p>Set</p>
                                <p>{i + 1}</p>
                            </div>
                            <div>
                                <p>Reps</p>
                                <TextField label="Reps" value={results[i].reps} name={`reps-${i}`} onChange={handleRepChange} InputProps={{endAdornment:<InputAdornment position="end">Reps</InputAdornment>}}/>
                            </div>
                            <div>
                                <p>Rest</p>
                                <TextField label="Rest" value={results[i].rest} name={`rest-${i}`} onChange={handleRestChange} InputProps={{endAdornment:<InputAdornment position="end">seconds</InputAdornment>}}/>
                            </div>

                        </form>)}) : sets.map((set, i) =>{
                    return (<form className={classes.form} key={`exercise${exercise.id}set${i+1}`}>
                            <div>
                                <p>Set</p>
                                <p>{i + 1}</p>
                            </div>
                            <div>
                                <p>Work</p>
                                <TextField label="Work" value={results[i].time} name={`work-${i}`} onChange={handleWorkChange} InputProps={{endAdornment:<InputAdornment position="end">seconds</InputAdornment>}}/>
                            </div>

                        </form>)})}
            <CardActions>
            </CardActions>
        </Card>
    )
}