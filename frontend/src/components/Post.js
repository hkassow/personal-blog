import Prism from "prismjs"
import "prismjs/themes/prism-okaidia.css"
import 'prismjs/components/prism-python'
import { useEffect } from "react"

function Post({post}) {
    useEffect(() => {
        console.log('PRISM IS HIGHLIGHTING')
        Prism.highlightAll() 
    })

    let innerHtml = {__html: post.body }
    return (
        <div>
            <h1> {post.title}</h1>
            <h2> Posted on: {post.pub_date} </h2>
            <h2> Last udated: {post.update_date} </h2>
            <p dangerouslySetInnerHTML={innerHtml}></p> 
        </div>
    )
}


export default Post