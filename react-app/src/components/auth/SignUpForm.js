import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux"
import { makeStyles } from '@material-ui/core/styles';
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';
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

const SignUpForm = () => {
  const [username, setUsername] = useState("");
  const [usernameErrors, setUsernameErrors] = useState("");
  const [email, setEmail] = useState("");
  const [emailErrors, setEmailErrors] = useState("");
  const [password, setPassword] = useState("");
  const [passwordErrors, setPasswordErrors] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [repeatPasswordErrors, setRepeatPasswordErrors] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const classes = useStyles()

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      await dispatch(signUp(username, email, password));
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <Card>
      <form onSubmit={onSignUp} className={classes.form}>
      <Typography variant='h3'>Sign Up</Typography>
          <TextField className={classes.input} error={usernameErrors !== ''} helperText={!username ? 'Please enter an username' : usernameErrors ? usernameErrors : null} value={username} label='Username' type='username' onChange={updateUsername} name="username" required/>
          <TextField className={classes.input} error={emailErrors !== ''} helperText={!email ? 'Please enter an email' : emailErrors ? emailErrors : null} value={email} label='Email' type='email' onChange={updateEmail} name="email" required/>
          <TextField className={classes.input} error={passwordErrors !== ''} helperText={!password ? 'Please enter a password' : passwordErrors ? passwordErrors : null} value={password} label='Password' type='password' onChange={updatePassword} name="password" required/>
          <TextField className={classes.input} error={repeatPasswordErrors !== ''} helperText={!repeatPassword ? 'Please repeat your password' : repeatPasswordErrors ? repeatPasswordErrors : null} value={repeatPassword} label='Repeat Password' type='password' onChange={updateRepeatPassword} name="password" required/>
        {/* <div>
          <label>User Name</label>
          <input
            type="text"
            name="username"
            onChange={updateUsername}
            value={username}
          ></input>
        </div>
        <div>
          <label>Email</label>
          <input
            type="text"
            name="email"
            onChange={updateEmail}
            value={email}
          ></input>
        </div>
        <div>
          <label>Password</label>
          <input
            type="password"
            name="password"
            onChange={updatePassword}
            value={password}
          ></input>
        </div>
        <div>
          <label>Repeat Password</label>
          <input
            type="password"
            name="repeat_password"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
          ></input>
        </div> */}
          <Button type="submit" className={classes.button} variant="contained">Sign Up</Button>
        {/* <button type="submit"></button> */}
      </form>
    </Card>
  );
};

export default SignUpForm;
