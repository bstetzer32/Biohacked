import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { makeStyles } from '@material-ui/core/styles';
import { Redirect } from "react-router-dom";
import { login } from "../../store/session";
import {FormControl, FormLabel, RadioGroup, TextField, Button, Radio, Card, Typography } from '@material-ui/core';


const useStyles = makeStyles((theme) => ({
    root: {
        width: '30%'
    },
    form: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    button: {
        width: '50%',
        margin: '0.5%'
    },
    input: {
        width: '50%',
        margin: '0.5%'
    }
}))

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [emailErrors, setEmailErrors] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordErrors, setPasswordErrors] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const classes = useStyles()

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      data.errors.forEach(error => {
        if (error.includes('email')) {
          setEmailErrors('Email provided not found.')
        }
        if (error.includes('password')) {
          setPasswordErrors('Password was incorrect.')
        }
        
      });
      setErrors(data.errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <Card>
      <form onSubmit={onLogin} className={classes.form}>
      <Typography variant='h3'>Log In</Typography>
        <FormControl className={classes.button}>
          <TextField error={emailErrors !== ''} helperText={!email ? 'Please enter an email' : emailErrors ? emailErrors : null} value={email} label='Email' type='email' onChange={updateEmail} name="email"/>
        </FormControl>
        <FormControl className={classes.button}>
          <TextField error={passwordErrors !== ''} helperText={!password ? 'Please enter a password' : passwordErrors ? passwordErrors : null} value={password} label='Password' type='password' onChange={updatePassword} name="password"/>
        </FormControl>
          <Button type="submit" className={classes.button} variant="contained">Login</Button>
      </form>
    </Card>
  );
};

export default LoginForm;
