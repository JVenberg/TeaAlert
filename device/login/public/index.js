
import { initializeApp } from 'https://www.gstatic.com/firebasejs/9.15.0/firebase-app.js';
import {
  getAuth,
  signOut,
  signInWithRedirect,
  onAuthStateChanged,
  GoogleAuthProvider
} from 'https://www.gstatic.com/firebasejs/9.15.0/firebase-auth.js';

const provider = new GoogleAuthProvider();
const firebaseConfig = {
  apiKey: "AIzaSyCiSr9kP46zvq8PbJHOqX95LXRXpsX7RMc",
  authDomain: "tea-alert.firebaseapp.com",
  databaseURL: "https://tea-alert-default-rtdb.firebaseio.com",
  projectId: "tea-alert",
  storageBucket: "tea-alert.appspot.com",
  messagingSenderId: "1090413450523",
  appId: "1:1090413450523:web:4a72cfed514ceb43ee6fbe"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

const API_KEY = 'AIzaSyCiSr9kP46zvq8PbJHOqX95LXRXpsX7RMc';

async function onSignIn(user) {
  const signoutBtn = document.getElementById('sign-out');
  signoutBtn.addEventListener('click', onSignOutClick);
  signoutBtn.disabled = false;

  const res = await fetch(`/token`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      'token': user.refreshToken,
    }),
  })
  if (res.ok) {
    console.log('Successfully wrote token');
  } else {
    console.error(`Error writing token: ${await res.text()}`);
  }
}

async function onSignOut() {
  const signoutBtn = document.getElementById('sign-out');
  try {
    const results = await signInWithRedirect(auth, provider);
  } catch (error) {
    console.error(error);
  }
  signoutBtn.disabled = true;
}

async function onSignOutClick() {
  try {
    await signOut(auth)
  } catch (error) {
    console.error(error);
  }
}

onAuthStateChanged(auth, async (user) => {
  if (user) {  // Logged in
    onSignIn(user);
  } else {  // Not logged in
    await onSignOut();
  }
});



