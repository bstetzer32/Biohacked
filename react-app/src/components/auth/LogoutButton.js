import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import {ListItemText} from "@material-ui/core"

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    dispatch(logout());
  };

  return <ListItemText onClick={onLogout}>Logout</ListItemText>;
};

export default LogoutButton;
