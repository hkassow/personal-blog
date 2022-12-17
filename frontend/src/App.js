import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'
import PostLayout from './components/PostLayout';

function App() {
  let [posts, setPosts] = useState(['No posts'])
  useEffect(()=> {
    fetch('http://127.0.0.1:8000/api/posts/', {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(r => r.json())
    .then(data => setPosts(data))
  },[])
  
  
  return (
    <div>
        <header>header</header>
          <PostLayout post={posts[posts.length - 1]}/>
        <footer>footer</footer>
    </div>
  );
}

export default App;
