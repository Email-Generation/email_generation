import "./App.css"
const SkeletonLoader = () => {
    return(
    <div className="loader" style={{width: "100%", height: "200px", borderRadius: 10, marginTop: 10}}>
        <div class="wrapper">
            <div class="line-1"/>
            <div class="line-2"/>
            <div class="line-3"/>
            <div class="line-4"/>
            <div class="line-5"/>
            <div class="line-6"/>
            <div class="line-7"/>
            <div class="line-8"/>
        </div>
    </div>
    )
}

export default SkeletonLoader