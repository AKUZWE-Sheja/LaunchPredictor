import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Define sample data representing launch distances and corresponding launch angles
# Sample data (launch distances in meters and launch angles in degrees)
launch_data = {
    'distance_meters': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'angle_degrees': [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
}

# Step 2: Convert the data into a pandas DataFrame
df_launch = pd.DataFrame(launch_data)

# Step 3: Split the data into training and testing sets
X_features = df_launch[['distance_meters']]  # Features
y_target = df_launch['angle_degrees']       # Target
X_train, X_test, y_train, y_test = train_test_split(X_features, y_target, test_size=0.2, random_state=42)

# Step 4: Create a linear regression model
regression_model = LinearRegression()

# Step 5: Train the model using the training data
regression_model.fit(X_train, y_train)

# Step 6: Make predictions on the testing data
y_predictions = regression_model.predict(X_test)

# Step 7: Evaluate the model's performance using mean square error
mean_sq_error = mean_squared_error(y_test, y_predictions)
print(f'Mean Squared Error: {mean_sq_error}')

# Step 8: Predict the launching angle for a new launch distance (e.g., 75 meters)
new_distance = np.array([[75]])
predicted_launch_angle = regression_model.predict(new_distance)
print(f'Predicted Launch Angle for 75 meters: {predicted_launch_angle[0]:.2f} degrees')
