import "./App.css";
const SkeletonLoader = () => {
	return (
		<div
			className="loader"
			style={{
				width: "100%",
				height: "200px",
				borderRadius: 10,
				marginTop: 10,
			}}
		>
			<div className="wrapper">
				<div className="line-1" />
				<div className="line-2" />
				<div className="line-3" />
				<div className="line-4" />
				<div className="line-5" />
				<div className="line-6" />
				<div className="line-7" />
				<div className="line-8" />
			</div>
		</div>
	);
};

export default SkeletonLoader;
