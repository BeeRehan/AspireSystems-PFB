import React from 'react';
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import { Link } from 'react-router-dom';

export default function Navbar(props) {
  return (
    <Box sx={{ width: '100%', bgcolor: 'background.paper' }}>
      <Tabs centered>
        <Tab as={Link} to={props.link} label={props.name} />
        <Tab as={Link} to={"/myprofile"} label="My Profile" />
        <Tab as={Link} to={"/logout"} label="Logout" />
      </Tabs>
    </Box>
  );
}