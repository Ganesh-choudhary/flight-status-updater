document.addEventListener('DOMContentLoaded', () => {
    fetchFlightStatus();
    setInterval(fetchFlightStatus, 60000); // Refresh every 60 seconds
  });
  
  async function fetchFlightStatus() {
    try {
      const response = await fetch('/api/flight-status/');
      if (response.ok) {
        const status = await response.json();
        updateFlightStatus(status);
      } else {
        console.error('Failed to fetch flight status:', response.statusText);
      }
    } catch (error) {
      console.error('Error fetching flight status:', error);
    }
  }
  
  function updateFlightStatus(status) {
    const statusTitle = document.getElementById('status-title');
    const statusDetails = document.getElementById('status-details');
  
    statusTitle.textContent = `Flight ${status.flight_number}: ${status.status}`;
    statusDetails.textContent = `Gate: ${status.gate}, Scheduled Time: ${status.scheduled_time}, Estimated Time: ${status.estimated_time}`;
  }
  