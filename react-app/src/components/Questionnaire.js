import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import {FormControl, FormLabel, RadioGroup, FormControlLabel, Button, Radio, Paper } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '2.5%'
    },
    control: {
        display: 'flex',
        padding: '2.5%',
        flexDirection: 'column',

    }
}))

export default function Questionnaire() {
    const [parq1, setParq1] = useState('')
    const [parq2, setParq2] = useState('')
    const [parq3, setParq3] = useState('')
    const [parq4, setParq4] = useState('')
    const [parq5, setParq5] = useState('')
    const [parq6, setParq6] = useState('')
    const [parq7, setParq7] = useState('')
    const [barbells, setBarbells] = useState('')
    const [dumbbells, setDumbbells] = useState('')
    // const [kettlebells, setKettlebells] = useState('')
    // const [kettlebells, setKettlebells] = useState('')
    const classes = useStyles()



    return (
        <Paper className={classes.root}>
            <form>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Has your doctor ever said that you have a heart condition and that you should only perform physical activity recommended by a doctor?
                    </FormLabel>
                    <RadioGroup name='parq1' onChange={(e)=>setParq1(e.target.value)} value={parq1}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Do you feel pain in your chest when you perform physical activity?
                    </FormLabel>
                    <RadioGroup name='parq2' onChange={(e)=>setParq2(e.target.value)} value={parq2}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        In the past month, have you had chest pain when you were not performing any physical activity?
                    </FormLabel>
                    <RadioGroup name='parq3' onChange={(e)=>setParq3(e.target.value)} value={parq3}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Do you lose your balance because of dizziness or do you ever lose consciousness? 
                    </FormLabel>
                    <RadioGroup name='parq4' onChange={(e)=>setParq4(e.target.value)} value={parq4}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Do you have a bone or joint problem that could be made worse by a change in your physical activity? 
                    </FormLabel>
                    <RadioGroup name='parq5' onChange={(e)=>setParq5(e.target.value)} value={parq5}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Is your doctor currently prescribing any medication for your blood pressure or for a heart condition? 
                    </FormLabel>
                    <RadioGroup name='parq6' onChange={(e)=>setParq6(e.target.value)} value={parq6}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Do you know of any other reason why you should not engage in physical activity? 
                    </FormLabel>
                    <RadioGroup name='parq7' onChange={(e)=>setParq7(e.target.value)} value={parq7}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
                <FormControl component='fieldset' className={classes.control}>
                    <FormLabel component="legend">
                        Do you have access to and feel comfortable using a standard barbell setup (freeheld, rack, and bench) with our provided exercise videos?
                    </FormLabel>
                    <RadioGroup name='barbells' onChange={(e)=>setBarbells(e.target.value)} value={barbells}>
                        <FormControlLabel value='yes' control={<Radio />} label='Yes'/>
                        <FormControlLabel value='no' control={<Radio />} label='No'/>
                    </RadioGroup>
                </FormControl>
            </form>
        </Paper>
    )
}