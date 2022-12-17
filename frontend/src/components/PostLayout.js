import profile_pic from '../images/profile_pic.jfif'
import Post from './Post'
const emailBtn = () => {
    fetch('http://127.0.0.1:8000/emailFunc')
    .then(r => console.log(r.text()))
}

function PostLayout({ post }) {
    return (
        <div id="page_layout">
            <div id="main_content">
                <div id="post_content">
                    {/* {% block child %}
                    {% endblock %} */}
                    <Post post={post}/>
                </div>
            </div>
            <div id="side_box">
                <div id="side_box_content">
                    <h1> Hunter Kassow </h1>
                    <img id='profile_image' src={profile_pic} alt="baby hunter"/>
                    <figure>
                        <figcaption>Other media</figcaption>
                        <ul>
                            <li><a href="https://www.linkedin.com/in/hunter-kassow/" target="_blank" rel="noopener noreferrer">Linkedin</a></li>
                            <li><a href="https://github.com/hkassow" target="_blank" rel="noopener noreferrer">Github</a></li>
                            <li><a href="mailto:hunterdkassow@gmail.com">hunterdkassow@gmail.com</a></li>
                        </ul>
            
                        <button onClick={() => emailBtn()}>TEST CLICK</button>
                    </figure>
                </div>
            </div>
        </div>
    )

}

export default PostLayout