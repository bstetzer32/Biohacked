import React, {useState} from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from "react-redux";
import LogoutButton from './auth/LogoutButton';
// import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import Link from '@material-ui/core/Link';
import Divider from '@material-ui/core/Divider';
import Drawer from '@material-ui/core/Drawer';
import Hidden from '@material-ui/core/Hidden';
import IconButton from '@material-ui/core/IconButton';
// import InboxIcon from '@material-ui/icons/MoveToInbox';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
// import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
// import MailIcon from '@material-ui/icons/Mail';
import MenuIcon from '@material-ui/icons/Menu';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles, useTheme } from '@material-ui/core/styles';

const drawerWidth = "160pt";

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  drawer: {
    [theme.breakpoints.up('sm')]: {
      width: drawerWidth,
      flexShrink: 0,
    },
  },
  appBar: {
      // backgroundImage: "url(/banner.png)",
      // backgroundSize: "contain",
      // backgroundPosition: "center",
      // height: "38%",
      backgroundColor: "#89d7ff",
      [theme.breakpoints.up('sm')]: {
        width: `calc(100% - ${drawerWidth})`,
        marginLeft: drawerWidth,
    },
  },
  menuButton: {
    marginRight: theme.spacing(2),
    [theme.breakpoints.up('sm')]: {
      display: 'none',
    },
  },
  // necessary for content to be below app bar
  toolbar: theme.mixins.toolbar,
  drawerPaper: {
    width: drawerWidth,
  },
  content: {
    flexGrow: 1
  },
  title: {
    fontWeight: "900",
    fontStyle: "italic",
    width: "100%"
  },
  navLink: {
    textDecoration: "none",
    "&:hover": {
      textDecoration: "underline"
    }
  },
  
}));

const NavBar = (props) => {
  const { window } = props;
  const classes = useStyles();
  const theme = useTheme();
  // console.log(theme.breakpoints.up('sm'))
  const [mobileOpen, setMobileOpen] = useState(false);
  const container = window !== undefined ? () => window().document.body : undefined;
  const user = useSelector(state => state.session.user)
  const loggedIn = user?.id
  
  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  const drawer = (
        <>

      <div className={classes.toolbar} />
      <Divider />
        <List>
            <NavLink className={classes.navLink} to="/" exact={true} activeClassName="active">
          <ListItem button>
              <ListItemText primary="Home"/>
          </ListItem>
            </NavLink>
          {!loggedIn 
          ?
            <>
              <NavLink className={classes.navLink} to="/login" exact={true} activeClassName="active">
            <ListItem button>
                <ListItemText primary="Login"/>
            </ListItem>
              </NavLink>
              <NavLink className={classes.navLink} to="/sign-up" exact={true} activeClassName="active">
            <ListItem button>
                <ListItemText primary="Sign Up"/>
          </ListItem>
              </NavLink>
          </>
          :
          <>
              <NavLink className={classes.navLink} to="/routines" exact={true} activeClassName="active">
            <ListItem button>
                <ListItemText primary="Routines"/>
            </ListItem>
              </NavLink>
              <NavLink className={classes.navLink} to="/results" exact={true} activeClassName="active">
            <ListItem button>
                <ListItemText primary="Results"/>
            </ListItem>
              </NavLink>
            <ListItem button>
              <LogoutButton />
            </ListItem>
          </>
          }

              <Link href="https://github.com/bstetzer32/Biohacked">
            <ListItem button>
                <ListItemText primary="GitHub"/>
            </ListItem>
              </Link>              
              <Link href="https://www.linkedin.com/in/ben-stetzer-9334881ba/">
            <ListItem button>
                <ListItemText primary="LinkedIn"/>
            </ListItem>
              </Link>

            <ListItem div>
                <ListItemText primary="Copyright 2021 Biohacked, LLC"/>
            </ListItem>
        </List>
        </>
  )

  return (
    <div className={classes.root}>
      <AppBar position="fixed" className={classes.appBar}>
        <Toolbar>
          <IconButton
            color="inherit"
            aria-label="open drawer"
            edge="start"
            onClick={handleDrawerToggle}
            className={classes.menuButton}
          >
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" noWrap className={classes.title}>
            Biohacked Fitness
          </Typography>
        </Toolbar>
      </AppBar>

      <nav className={classes.drawer} aria-label="mailbox folders">
        <Hidden smUp implementation="css">
          <Drawer
            container={container}
            variant="temporary"
            anchor={theme.direction === 'rtl' ? 'right' : 'left'}
            open={mobileOpen}
            onClose={handleDrawerToggle}
            classes={{
              paper: classes.drawerPaper,
            }}
            ModalProps={{
              keepMounted: true
            }}
          >
            {drawer}
          </Drawer>
        </Hidden>
        <Hidden xsDown implementation="css">
          <Drawer
            classes={{
              paper: classes.drawerPaper,
            }}
            variant="permanent"
            open
          >
            {drawer}
          </Drawer>
        </Hidden>
      </nav>
      <main className={classes.content}>
        <div className={classes.toolbar} />
        {props.children}
        </main>
    </div>
  );
}

export default NavBar;
